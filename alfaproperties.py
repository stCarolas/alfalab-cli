#!/usr/bin/env python3
# Extract settings from property files from ~/.config/alfa/settings.cfg

import configparser, argparse

def get_cli_args():
    parser = argparse.ArgumentParser(description='Get properties for alfalab cli')
    parser.add_argument('key',
                        metavar = 'key',
                        type = str, 
                        nargs = 1,
                        help = 'property key')
    return parser.parse_args()

class Config():
    path = "/home/stcarolas/.config/alfa/settings.cfg"

    def get_value(self, section, key):
        config = configparser.ConfigParser()
        config.read(self.path)
        return config[section][key]
        
if __name__ == '__main__':
    args = get_cli_args()
    print(Config().get_value("global",args.key[0]))