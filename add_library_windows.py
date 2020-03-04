import sys
import os
import subprocess
import xml.etree.ElementTree

if __name__ == "__main__":
  assert len(sys.argv) <= 2, 'Only takes one argument \'-u\' to automatically add JUnit'

  if not os.path.isdir('lib'):
    subprocess.call('mkdir lib')

  urls = []
  if len(sys.argv) == 1:
    # read user input
    while True:
      user_in = input('Enter URL or Enter x to quit: ')
      if user_in != 'x':
        urls.append(user_in)
      else:
        break
  else:
    assert sys.argv[1] == '-u', 'Only takes one argument \'-u\' to automatically add JUnit'
    urls.append('https://search.maven.org/remotecontent?filepath=org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar')
    urls.append('https://search.maven.org/remotecontent?filepath=junit/junit/4.13/junit-4.13.jar')

  et = xml.etree.ElementTree.parse('.classpath')

  for url in urls:
    filename = url.split('/')[-1]
    cmd = 'iwr %s -outf lib/%s' % (url, filename)
    subprocess.call('C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe %s' % cmd, shell=True)

    # Append new tag: <a x='1' y='abc'>body text</a>
    new_tag = xml.etree.ElementTree.SubElement(et.getroot(), 'classpathentry')
    new_tag.attrib['kind'] = 'lib' # must be str; cannot be an int
    new_tag.attrib['path'] = 'lib/%s' % filename

  et.write('.classpath')