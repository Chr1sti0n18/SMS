; Script de Instalação para o seu programa SMS.exe
[Setup]
AppName=SMS
AppVersion=1.0
DefaultDirName={pf}\SMS
DefaultGroupName=SMS
OutputDir=C:\Labs\Python\Personal_projects\Gerenciamento_de_estoque\SMS_main\Gerenciamento_de_estoque_padaria\output\SMS\dist
OutputBaseFilename=SMS_installer
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "portuguese"; MessagesFile: "compiler:Languages\Portuguese.isl"

[Files]
Source: ".\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\SMS"; Filename: "{app}\SMS.exe"
Name: "{commondesktop}\SMS"; Filename: "{app}\SMS.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Criar atalho na Área de Trabalho"; GroupDescription: "Opções adicionais:"; Flags: unchecked
