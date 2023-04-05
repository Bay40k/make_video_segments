import threading
import time
from pathlib import Path

import MainForm
import wx

import make_segments


class App(wx.App):
    def __init__(self, redirect=False, **kwds):
        try:
            from ctypes import OleDLL

            # Turn on high-DPI awareness to make sure rendering is sharp on big
            # monitors with font scaling enabled.
            OleDLL("shcore").SetProcessDpiAwareness(1)

        except AttributeError:
            # We're on a non-Windows box.
            pass

        except (OSError, ImportError):
            # exc.winerror is often E_ACCESSDENIED (-2147024891/0x80070005).
            # This occurs after the first run, when the parameter is reset in the
            # executable's manifest and then subsequent calls raise this exception
            # See last paragraph of Remarks at
            # [https://msdn.microsoft.com/en-us/library/dn302122(v=vs.85).aspx](https://msdn.microsoft.com/en-us/library/dn302122(v=vs.85).aspx)
            pass

        super().__init__(**kwds)


class MainFrame(MainForm.MainFrame):
    def __init__(self, parent):
        self.input_file_selected = False
        self.output_dir_selected = False
        MainForm.MainFrame.__init__(self, parent)
        self.SetClientSize(self.FromDIP(wx.Size(508, 350)))
        self.Show()
        self.default_output_text = self.OutputText.GetLabelText()

    def set_output_dir(self, event):
        print("Directory selected")
        make_segments.OUTPUT_DIR = Path(event.GetPath())
        print(make_segments.OUTPUT_DIR)
        self.output_dir_selected = True
        if event.GetPath() == "":
            self.output_dir_selected = False

    def set_input_file(self, event):
        print("File selected")
        file_path = Path(event.GetPath())
        make_segments.INPUT_VIDEO_FILEPATH = file_path
        make_segments.INPUT_VIDEO_FILENAME = file_path.stem
        print(make_segments.INPUT_VIDEO_FILEPATH)
        self.OutputDir.SetPath(str(file_path.parent))
        event.SetPath(str(file_path.parent))
        self.set_output_dir(event)
        self.input_file_selected = True
        if event.GetPath() == "":
            self.input_file_selected = False

    def on_submit_click(self, event):
        print("Submit button clicked")
        if not self.input_file_selected:
            self.OutputText.SetLabel("Please select an input file")
        elif not self.output_dir_selected:
            self.OutputText.SetLabel("Please select an output directory")
        else:
            self.OutputText.SetLabel(self.default_output_text)
        self.OutputText.Show()
        if self.default_output_text == self.OutputText.GetLabelText():
            self.run_make_segments()
            self.OutputText.SetLabel("Done")
            self.ProgressBar.SetValue(100)

    def fade_in_checked(self, event):
        print("Fade in checked")
        if self.FadeInCheck.GetValue():
            self.FadeInDuration.Enable()
            self.FadeInSlider.Enable()
        else:
            self.FadeInDuration.Disable()
            self.FadeInSlider.Disable()

    def fade_out_checked(self, event):
        print("Fade out checked")
        if self.FadeOutCheck.GetValue():
            self.FadeOutDuration.Enable()
            self.FadeOutSlider.Enable()
        else:
            self.FadeOutDuration.Disable()
            self.FadeOutSlider.Disable()

    def on_segment_length_slider(self, event):
        self.SegmentLength.SetValue(self.SegmentLengthSlider.GetValue())

    def on_fade_in_slider(self, event):
        self.FadeInDuration.SetValue(self.FadeInSlider.GetValue())

    def on_fade_out_slider(self, event):
        self.FadeOutDuration.SetValue(self.FadeOutSlider.GetValue())

    def on_segment_length(self, event):
        if self.SegmentLength.GetValue() >= self.SegmentLengthSlider.GetMax():
            self.SegmentLengthSlider.SetValue(self.SegmentLengthSlider.GetMax())
        self.SegmentLengthSlider.SetValue(self.SegmentLength.GetValue())

    def on_fade_in_duration(self, event):
        self.FadeInSlider.SetValue(self.FadeInDuration.GetValue())

    def on_fade_out_duration(self, event):
        self.FadeOutSlider.SetValue(self.FadeOutDuration.GetValue())

    def run_make_segments(self):
        self.ProgressBar.SetValue(0)
        self.OutputText.SetLabel("Running...")
        print("Running make_segments")
        make_segments.SEGMENT_LENGTH = self.SegmentLength.GetValue()
        make_segments.FADE_IN_DURATION = self.FadeInDuration.GetValue()
        make_segments.FADE_OUT_DURATION = self.FadeOutDuration.GetValue()

        make_segments_thread = threading.Thread(target=make_segments.make_segments)
        make_segments_thread.start()
        while make_segments_thread.is_alive():
            self.ProgressBar.Pulse()
            time.sleep(0.1)
            wx.Yield()

        if not self.FadeInCheck.GetValue() and not self.FadeOutCheck.GetValue():
            print("Fading disabled")
            return

        if not self.FadeInCheck.GetValue():
            make_segments.FADE_IN_DURATION = 0
        if not self.FadeOutCheck.GetValue():
            make_segments.FADE_OUT_DURATION = 0
        self.OutputText.SetLabel("Fading segments...")
        print("Fading segments")

        make_segments_thread = threading.Thread(target=make_segments.fade_segments)
        make_segments_thread.start()
        while make_segments_thread.is_alive():
            self.ProgressBar.Pulse()
            time.sleep(0.1)
            wx.Yield()


app = App(False)
frame = MainFrame(None)
app.MainLoop()
