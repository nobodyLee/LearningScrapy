import os
import sys

from scrapy.cmdline import execute


project_path = os.path.dirname(__file__)
sys.path.append(project_path)
execute(['scrapy', 'crawl', 'images'])

