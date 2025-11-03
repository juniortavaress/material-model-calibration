; ====================================================
; Instalador Inno Setup para MMCA (PyQt)
; ====================================================

[Setup]
AppName=MMCA
AppVersion=1.0
DefaultDirName={pf}\MMCA
DefaultGroupName=MMCA
OutputDir=installer_output
OutputBaseFilename=MMCA_Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
AllowNoIcons=no
DisableProgramGroupPage=no

[Languages]
Name: "english"; MessagesFile: "compiler:Languages\English.isl"

[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion; DestName: "mmca.exe"
Source: "README.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "LICENSE.txt"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\MMCA"; Filename: "{app}\mmca.exe"
Name: "{userdesktop}\MMCA"; Filename: "{app}\mmca.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop icon"; GroupDescription: "Additional tasks:"; Flags: unchecked

[Run]
Filename: "{app}\mmca.exe"; Description: "Launch MMCA"; Flags: nowait postinstall skipifsilent
