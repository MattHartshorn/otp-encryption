import argparse

class HelpAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(HelpAction, self).__init__(option_strings, dest, nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if (values == None or values == ""):
            print(parser.format_help())
            parser.exit()

        actions = [action for action in parser._actions if isinstance(action, argparse._SubParsersAction)]

        for action in actions:
            for choice, subparser in action.choices.items():
                if (choice == values):
                    print(subparser.format_help())
                    parser.exit()
                    
        parser.error("Unknown command '{0}'".format(values))

