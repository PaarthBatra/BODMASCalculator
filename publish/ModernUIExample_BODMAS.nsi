;NSIS Modern User Interface
;Welcome/Finish Page Example Script
;Written by Joost Verburg

;--------------------------------
;Include Modern UI

  !include "MUI2.nsh"

;--------------------------------
;General

	!define APPNAME "BODMAS Calculator"
	!define COMPANYNAME "VersionPB"
	!define DESCRIPTION "It Does Maths by BODMAS Rule"
	# These three must be integers
	!define VERSIONMAJOR 3
	!define VERSIONMINOR 0
	!define VERSIONBUILD 0
	# These will be displayed by the "Click here for support information" link in "Add/Remove Programs"
	# It is possible to use "mailto:" links in here to open the email client
	!define HELPURL "http://www.versionpb.co.in" # "Support Information" link
	!define UPDATEURL "http://www.versionpb.co.in" # "Product Updates" link
	!define ABOUTURL "http://www.versionpb.co.in" # "Publisher" link
	!define INSTALLSIZE 92586
	
	;Request application privileges for Windows Vista
	RequestExecutionLevel admin
  
	;Default installation folder
	InstallDir "$PROGRAMFILES\${COMPANYNAME}\${APPNAME}"
  
	;Name and file
	Name "${COMPANYNAME} - ${APPNAME}"
	Icon "Calculator.ico"
	UninstallIcon "Calculator.ico"
	outFile "Bodmas_Calculator_NSIS.exe"

;--------------------------------
;Interface Settings

  !define MUI_ABORTWARNING
  !define MUI_ICON "Calculator.ico"
  !define MUI_UNICON "Calculator.ico"

;--------------------------------
;Pages

  !insertmacro MUI_PAGE_WELCOME
  !insertmacro MUI_PAGE_LICENSE "license.rtf"
  !insertmacro MUI_PAGE_COMPONENTS
  !insertmacro MUI_PAGE_DIRECTORY
  !insertmacro MUI_PAGE_INSTFILES
  !insertmacro MUI_PAGE_FINISH

  !insertmacro MUI_UNPAGE_WELCOME
  !insertmacro MUI_UNPAGE_CONFIRM
  !insertmacro MUI_UNPAGE_INSTFILES
  !insertmacro MUI_UNPAGE_FINISH

;--------------------------------
;Languages

  !insertmacro MUI_LANGUAGE "English"

;--------------------------------
;Installer Sections

Section "BODMAS Calculator Installers" FilesADD
	
	# Files for the install directory
	setOutPath $INSTDIR
	
	# Copy main executable, assets, license and readme
	file "..\dist\Calculator\Calculator.exe"
	file "..\pbcabtdll"
	file "..\Exe\pkldll"
	file "Calculator.ico"
	file "/oname=readme.txt" "..\Exe\READ-ME.txt"
	file "license.rtf"

	# Copy the PyInstaller-created python dependency directory recursively
	SetOutPath "$INSTDIR\_internal"
	file /r "..\dist\Calculator\_internal\*.*"

	# Reset out path to base directory
	SetOutPath $INSTDIR

	# Start Menu
	createDirectory "$SMPROGRAMS\${COMPANYNAME}"
	createShortCut "$SMPROGRAMS\${COMPANYNAME}\${APPNAME}.lnk" "$INSTDIR\Calculator.exe" "" "$INSTDIR\Calculator.ico"
	CreateShortCut "$DESKTOP\${APPNAME}.lnk" "$INSTDIR\Calculator.exe" "" "$INSTDIR\Calculator.ico"
	
	# Registry information for add/remove programs
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "DisplayName" "${COMPANYNAME} - ${APPNAME}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "UninstallString" "$\"$INSTDIR\uninstall.exe$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "QuietUninstallString" "$\"$INSTDIR\uninstall.exe$\" /S"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "InstallLocation" "$\"$INSTDIR$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "DisplayIcon" "$\"$INSTDIR\Calculator.ico$\""
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

	# Uninstaller - See function un.onInit and section "uninstall" for configuration
	writeUninstaller "$INSTDIR\uninstall.exe"

SectionEnd

;--------------------------------
;Descriptions

  ;Language strings
  LangString DESC_FilesADD ${LANG_ENGLISH} "This Section contains all installables for BODMAS Calculator to work properly on your machine."

  ;Assign language strings to sections
  !insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
    !insertmacro MUI_DESCRIPTION_TEXT ${FilesADD} $(DESC_FilesADD)
  !insertmacro MUI_FUNCTION_DESCRIPTION_END

;--------------------------------
;Uninstaller Section

Section "Uninstall"

	# Remove shortcuts
	delete "$SMPROGRAMS\${COMPANYNAME}\${APPNAME}.lnk"
	delete "$DESKTOP\${APPNAME}.lnk"
	# Try to remove the Start Menu folder - this will only happen if it is empty
	rmDir "$SMPROGRAMS\${COMPANYNAME}"

	# Remove files
	delete "$INSTDIR\Calculator.exe"
	delete "$INSTDIR\pbcabtdll"
	delete "$INSTDIR\pkldll"
	delete "$INSTDIR\Calculator.ico"
	delete "$INSTDIR\readme.txt"
	delete "$INSTDIR\license.rtf"
	delete "$INSTDIR\uninstall.exe"

	# Remove internal files recursively
	rmDir /r "$INSTDIR\_internal"

	# Try to remove the install directory - this will only happen if it is empty
	rmDir "$INSTDIR"

	# Remove uninstaller information from the registry
	DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}"

SectionEnd