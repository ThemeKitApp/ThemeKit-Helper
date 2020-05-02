from themekitcli.logger import printc
from terminaltables import AsciiTable
from colorama import Fore
from zipfile import ZipFile, ZIP_DEFLATED
import os, plistlib

def options():
    try:
        while True:
            printc("ThemeKit Helper - Max Bridgland - v1.0", color="green", style="bright")
            printc("Choose From The Following Options:")
            options = [
                ['Option', 'Description'],
                ['0', '[B]undle ThemeKit Theme'],
                ['1', '[G]enerate Info.plist'],
                ['2', '[E]xit ThemeKit CLI']
            ]
            table = AsciiTable(options)
            printc(table.table, color="LIGHTRED_EX", style="BRIGHT")
            ans = input(Fore.LIGHTRED_EX + "# or Letter > " + Fore.RESET)
            if ans.lower() == "0" or ans.lower() == "b":
                bundle()
                break
            elif ans.lower() == "1" or ans.lower() == "g":
                plist_attrs = genplist()
                printc("Enter A Path To Output Your Info.plist:", color="GREEN")
                os.makedirs(os.path.realpath(plist_attrs['DisplayName'] + '-Gen'))
                with open(os.path.realpath(plist_attrs['DisplayName'] + '-Gen/Info.plist'), 'wb') as pf:
                    plistlib.dump(plist_attrs, pf)
                printc("New Info.plist Written To:", os.path.realpath(plist_attrs['DisplayName'] + '-Gen/Info.plist'), color="GREEN", style="BRIGHT")
                break
            elif ans.lower() == "2" or ans.lower() == "e":
                printc("Goodbye!", color="LIGHTRED_EX", style="BRIGHT")
                exit(0)
            else:
                printc("Unknown Option. Please Try Again!", color="RED", style="BRIGHT")
    except KeyboardInterrupt:
        exit()
        
def bundle():
    try:
        printc("Does your bundle already have an Info.plist? [Y\\n, default=no]:", color="BLUE", style="BRIGHT")
        alr = input("> ")
        has_plist = False
        if alr.lower() == "y":
            has_plist = True
            pass
        else:
            plist_attrs = genplist()
        path = None
        while True:
            printc("Enter The Path to Your Theme's .bundle:", color="LIGHTBLUE_EX", style="BRIGHT")
            ip = input("> ").strip()
            if not os.path.exists(os.path.realpath(ip)):
                printc("Error! File/Folder Not Found. Try Again.", color="RED", style="BRIGHT")
                pass
            else:
                bid = None
                if not has_plist:
                    bid = plist_attrs['BundleIdentifier']
                    path = os.path.realpath(ip)
                    with open(os.path.realpath(path + "/Info.plist"), 'wb') as f:
                        plistlib.dump(plist_attrs, f)
                else:
                    with open(os.path.realpath(path + "/Info.plist"), 'rb') as f:
                        obj = plistlib.load(f)
                        bid = obj.get('BundleIdentifier')
                        if not bid:
                            printc("It seems your Info.plist is malformed.\nPlease delete it and restart the program using our Info.plist Wizard next time!", color="RED", style="BRIGHT")
                            exit(1)
                    with ZipFile(bid + '.zip', 'w', ZIP_DEFLATED) as zf:
                        for root, _, files in os.walk(path):
                            for file in files:
                                zf.write(os.path.join(root, file))
    except KeyboardInterrupt:
        exit()
        
    
            
def genplist():
    try:
        while True:
            attrs = {}
            printc("Theme Name:", color="BLUE", style="BRIGHT")
            attrs['DisplayName'] = input("> ")
            printc("Your Name:", color="BLUE", style="BRIGHT")
            attrs['Author'] = input("> ")
            printc("Theme Version (Semantic):", color="BLUE", style="BRIGHT")
            attrs['Version'] = input("> ")
            printc("Your Website:", color="BLUE", style="BRIGHT")
            attrs['URL'] = input("> ")
            if attrs['URL'].startswith("http"):
                attrs['URL'] = attrs['URL'].strip("://")[1]
            website_sp = attrs['URL'].split('.')
            website_sp.reverse()
            printc("Your Bundle ID [" + ".".join(website_sp) + "." + attrs['DisplayName'].replace(" ", "") + "]:", color="BLUE", style="BRIGHT")
            attrs['BundleIdentifier'] = input("> ")
            if len(attrs['BundleIdentifier']) <= 1:
                attrs['BundleIdentifier'] = ".".join(website_sp) + "." + attrs['DisplayName'].replace(" ", "")
            printc("Use Preview Features? (Requires: Settings, Messages, Mail, Music (iTunes), Preview) [Y\\n, default=no]:", color="BLUE", style="BRIGHT")
            ans = input("> ")
            attrs['usesFeatures'] = False
            if ans.lower() == "y":
                attrs['usesFeatures'] = True
            printc("Confirm Attributes:", color="GREEN", style="BRIGHT")
            table = [
                ['Attr.', 'Value']
            ]
            for k, v in attrs.items():
                table.append([k, v])
            ttable = AsciiTable(table)
            printc(ttable.table, color="LIGHTGREEN_EX", style="BRIGHT")
            res = input("[Y\\n, default=yes]> ")
            if res.lower() == "n":
                pass
            else:
                return attrs
    except KeyboardInterrupt:
        exit()

        
    