import re
import os
import subprocess
from sys import platform
from errors import ValidationError, UnsupportedPlatformError

class ScreamingFrogAnalyser(object):
    def __init__(self, website_urls,
                 outputfolder='',
                 export_tabs=False,
                 export_reports=False,
                 export_bulk_exports=False):

        self._website_urls = website_urls
        self._output_folder = '--output-folder ' + outputfolder
        self._export_tabs = export_tabs
        self._export_reports = export_reports
        self.export_bulk_exports = export_bulk_exports

        # This will populate with a list of folders that Screaming Frog Creates via --timestamped folder:
        self._sf_folders = []

        if self._output_folder == '':
            raise ValidationError('You must choose a valid output folder for your Screaming Frog Crawls',
                                 'outputfolder=""')

        # Creating the command based upon the Operating System:
        self._create_command()
        self._command_updater()

    def _create_command(self):
        if platform == "linux" or platform == "linux2":
            # Linux
            self._sf_command = 'screamingfrogseospider --headless --save-crawl'
        elif platform == "darwin":
            # OS X
            self._sf_command = '/Applications/Screaming\ Frog\ SEO\ Spider.app/Contents/MacOS/ScreamingFrogSEOSpiderLauncher --headless --save-crawl'
        elif platform == "win32":
            # Windows...
            raise UnsupportedPlatformError("Windows Is Currently Not Supported", 'Please stop using windows!')

    def _add_reports(self):
        for _, argument in zip([self._export_tabs, self._export_reports, self.export_bulk_exports],
                    ['--export-tabs', '--save-report', '--bulk-export']):
            if _ is not False:
                self.sf_command = self.sf_command + f' {argument} "{_}"'
            else:
                # This will just save the generic .seospider crawl
                pass

    def _parse_subprocess_text(self, subprocess_text):
        directory = re.findall('(?<=Output directory:)(.*?)(?=\n)',
                       str(subprocess_text.decode('utf-8')))
        try:
            return directory[0].strip()
        except IndexError:
            raise ValidationError('No folder was created, check your output folder and export settings', 'Incorrect Response')

    def _command_updater(self):
        self.sf_command = self._sf_command + ' ' + self._output_folder + ' --timestamped-output'
        print(f"Please make sure that the {self._output_folder} is a valid destination! \n")
        self._add_reports()
        print(self.sf_command)

    # Execution Functions
    def run_screaming_headless_frog(self, website):
        final_command = self.sf_command + ' --crawl ' + website
        screaming_frog=subprocess.run(final_command,
        shell=True,
        capture_output=True)
        return screaming_frog

    # Run Multiple Websites:
    def run_crawls(self):
        for website in self._website_urls:
            # 1. Crawl the website:
            output = self.run_screaming_headless_frog(website)
            # 2. Store the crawled files:
            resp = self._parse_subprocess_text(output.stdout)
            if isinstance(resp, str):
                self._sf_folders.append(resp)
            else:
                raise ValidationError('No folder was created, check your output folder and export settings', 'Incorrect Response')
            print(f'Successfully Crawled {website}')
            print('\n' + '----' + '\n')
