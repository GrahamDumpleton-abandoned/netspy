from setuptools import setup

setup(
  name = "netspy",
  version = "1.0.0",
  description = "GUI debugger for OSE message system.",
  author = "Graham Dumpleton",
  author_email = "Graham.Dumpleton@gmail.com",
  packages = ['netspy'],
  scripts = [ 'scripts/netspy', 'scripts/netspy-registry',
              'scripts/netspy-reports' ],
)
