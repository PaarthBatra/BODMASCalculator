# This installs the Python 3 / PyQt6 BODMAS Calculator, creates start menu & desktop shortcuts, builds an uninstaller, and
# adds uninstall information to the registry for Add/Remove Programs

!define APPNAME "Bodmas Calculator"
!define COMPANYNAME "VersionPB"
!define DESCRIPTION "It Does Maths by BODMAS Rule"
# These three must be integers
!define VERSIONMAJOR 3
!define VERSIONMINOR 0
!define VERSIONBUILD 0
# These will be displayed by the "Click here for support information" link in "Add/Remove Programs"
!define HELPURL "http://www.versionpb.co.in" # "Support Information" link
!define UPDATEURL "http://www.versionpb.co.in" # "Product Updates" link
!define ABOUTURL "http://www.versionpb.co.in" # "Publisher" link
# This is the size (in kB) of all the files copied into "Program Files"
!define INSTALLSIZE 92586

RequestExecutionLevel admin ;Require admin rights on NT6+ (When UAC is turned on)

InstallDir "$PROGRAMFILES\${COMPANYNAME}\${APPNAME}"

# license file in RTF format
LicenseData "license.rtf"
# This will be in the installer/uninstaller's title bar
Name "${COMPANYNAME} - ${APPNAME}"
Icon "..\Profile_Malaysia.ico"
outFile "Bodmas_Calculator_NSIS.exe"

!include LogicLib.nsh

# Just three pages - license agreement, install location, and installation
page license
page directory
Page instfiles

!macro VerifyUserIsAdmin
UserInfo::GetAccountType
pop $0
${If} $0 != "admin" ;Require admin rights on NT4+
        messageBox mb_iconstop "Administrator rights required!"
        setErrorLevel 740 ;ERROR_ELEVATION_REQUIRED
        quit
${EndIf}
!macroend

function .onInit
	setShellVarContext all
	!insertmacro VerifyUserIsAdmin
functionEnd

section "install"
	# Files for the install directory
	setOutPath $INSTDIR

	# Copy main executable, assets, license and readme
	file "..\dist\Calculator\Calculator.exe"
	file "..\pbcabtdll"
	file "..\Exe\pkldll"
	file "..\Profile_Malaysia.ico"
	file "/oname=readme.txt" "..\Exe\READ-ME.txt"
	file "license.rtf"

	# Copy the PyInstaller-created python dependency directory recursively
	SetOutPath "$INSTDIR\_internal"
	file /r "..\dist\Calculator\_internal\*.*"

	# Reset out path to base directory
	SetOutPath $INSTDIR

	# Uninstaller - See function un.onInit and section "uninstall" for configuration
	writeUninstaller "$INSTDIR\uninstall.exe"

	# Start Menu & Desktop shortcuts
	createDirectory "$SMPROGRAMS\${COMPANYNAME}"
	createShortCut "$SMPROGRAMS\${COMPANYNAME}\${APPNAME}.lnk" "$INSTDIR\Calculator.exe" "" "$INSTDIR\Profile_Malaysia.ico"
	CreateShortCut "$DESKTOP\${APPNAME}.lnk" "$INSTDIR\Calculator.exe" "" "$INSTDIR\Profile_Malaysia.ico"

	# Registry information for add/remove programs
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "DisplayName" "${COMPANYNAME} - ${APPNAME}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "UninstallString" "$\"$INSTDIR\uninstall.exe$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "QuietUninstallString" "$\"$INSTDIR\uninstall.exe$\" /S"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "InstallLocation" "$\"$INSTDIR$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "DisplayIcon" "$\"$INSTDIR\Profile_Malaysia.ico$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "Publisher" "$\"${COMPANYNAME}$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "HelpLink" "$\"${HELPURL}$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "URLUpdateInfo" "$\"${UPDATEURL}$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "URLInfoAbout" "$\"${ABOUTURL}$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "DisplayVersion" "$\"${VERSIONMAJOR}.${VERSIONMINOR}.${VERSIONBUILD}$\""
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "VersionMajor" ${VERSIONMAJOR}
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "VersionMinor" ${VERSIONMINOR}
	# There is no option for modifying or repairing the install
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "NoModify" 1
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "NoRepair" 1
	# Set the ESTIMATEDSIZE constant so Add/Remove Programs can report it accurately
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "EstimatedSize" ${INSTALLSIZE}
sectionEnd

# Uninstaller

function un.onInit
	SetShellVarContext all

	#Verify the uninstaller - last chance to back out
	MessageBox MB_OKCANCEL "Permanantly remove ${APPNAME}?" IDOK next
		Abort
	next:
	!insertmacro VerifyUserIsAdmin
functionEnd

section "uninstall"
	# Remove Start Menu launcher
	delete "$SMPROGRAMS\${COMPANYNAME}\${APPNAME}.lnk"
	delete "$DESKTOP\${APPNAME}.lnk"
	# Try to remove the Start Menu folder - this will only happen if it is empty
	rmDir "$SMPROGRAMS\${COMPANYNAME}"

	# Remove files
	delete "$INSTDIR\Calculator.exe"
	delete "$INSTDIR\pbcabtdll"
	delete "$INSTDIR\pkldll"
	delete "$INSTDIR\Profile_Malaysia.ico"
	delete "$INSTDIR\readme.txt"
	delete "$INSTDIR\license.rtf"
	delete "$INSTDIR\uninstall.exe"

	# Remove internal files recursively
	rmDir /r "$INSTDIR\_internal"

	# Try to remove the install directory - this will only happen if it is empty
	rmDir "$INSTDIR"

	# Remove uninstaller information from the registry
	DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}"
sectionEnd