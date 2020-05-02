from themekitcli.menus import options
def main():
    try:
        options()
    except KeyboardInterrupt:
        exit()
    
if __name__ == "__main__":
    main()