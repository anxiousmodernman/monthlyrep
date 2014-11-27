import sys
import argparse

from report.monthly import Unsubscribes, Opens, Profile



    # def render_excel(self, output_file):
    #     writer = pd.ExcelWriter(output_file)
    #     self._unsubs_by_category.to_excel(writer, 'unsubs')
    #     self._industry_subs.to_excel(writer, 'industry')
    #     print 'Writing output file to directory: %s' % os.path.abspath('.')
    #     writer.save()



def do_open_click(filename):
    report = Opens(filename)
    output_filename = 'processed_opens.xls'  # todo generate better names
    report.render_excel(output_filename)
    pass


def do_profile_completion(filename):
    report = Profile(filename)
    output_filename = 'processed_profile.xls'
    report.render_excel(output_filename)
    pass


def do_unsubs(filename):
    """
    Top-level routine for processing monthly unsubscribe Excel reports.

    Call like this, assuming mrep.py is on your system PATH:

    $ python mrep.py unsubs FILENAME.xls

    """
    report = Unsubscribes(filename)
    output_filename = 'processed_unsubs.xls'  # todo generate better names
    report.render_excel(output_filename)


def main(args):
    """
    This is the main routine for the mrep.py program.

    First we process args from the command line with builtin argparse module.
    You can read about argparse in Hellmann's book Python Standard Library By Example

    The first argument passed to mrep.py is interpreted as the 'command'. The
    following commands are supported:

    - unsubs
    - pcomp
    - opens

    The second argument is a filename representing the Excel doc to process.

    Depending on the command passed, mrep.py will hand control to a function
    that will be responsible for instantiating an instance of a particular kind
    of report, processing the data, and writing out a 'processed' Excel document.

    

    """
    cmd_parser = argparse.ArgumentParser(description='Process monthly report files')
    cmd_parser.add_argument('command', type=str)
    cmd_parser.add_argument('file_input', type=str)
    opts = cmd_parser.parse_args(args)

    if opts.command == 'unsubs':
        do_unsubs(opts.file_input)
    elif opts.command == 'pcomp':
        do_profile_completion(opts.file_input)
    elif opts.command == 'opens':
        do_open_click(opts.file_input)
    else:
        raise NotImplementedError('Command not recognized')


if __name__ == '__main__':
    # pass in arguments from command line with sys.argv
    main(sys.argv[1:])
