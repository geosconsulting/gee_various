import argparse

foo_default=None

class BarAction(argparse.Action):
    def __call__(self,parser,namespace,values,option_string=None):
        didfoo=getattr(namespace,'foo',foo_default)
        if(didfoo == foo_default):
            parser.error( "foo before bar!")
        else:
            setattr(namespace,self.dest,values)

parser=argparse.ArgumentParser()
parser.add_argument('--foo',default=foo_default)
parser.add_argument('--bar',action=BarAction,help="Only use this if --foo is set")

#testing.
print parser.parse_args('--foo baz'.split())
print parser.parse_args('--foo baz --bar cat'.split())
print parser.parse_args('--bar dog'.split())