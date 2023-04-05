# Import Modules
import optparse
import os
from toolkit import processor as ps


def main():
    usage = "usage: %prog [options] "
    Version = "%prog 0.0.1"

    parser = optparse.OptionParser(usage=usage, version=Version)

    parser.add_option('-i', '--input', type='string', dest='inputfile',
                      help="File Input Path For Encryption", default=None)

    parser.add_option('-o', '--output', type="string", dest='outputfile',
                      help="File Output Path For Saving Encrypter Cipher", default=".")

    parser.add_option('-p', '--password', type="string", dest='password',
                      help="Provide Password For Encrypting File", default=None)

    (options, args) = parser.parse_args()

    # Input Conditions Checkings
    if not options.inputfile or not os.path.isfile(options.inputfile):
        print("[Error] Please Specify Input File Path")
        exit(0)
    if not options.outputfile or not os.path.isdir(options.outputfile):
        print("[Error] Please Specify Output Path")
        exit(0)
    if not options.password:
        print("[Error] No Password Input")
        exit(0)

    inputfile = options.inputfile
    outputfile = os.path.join(options.outputfile, os.path.basename(options.inputfile).split('.')[0] + '.ssb')
    password = options.password
    base = os.path.basename(inputfile).split('.')[1]
    work = "E"

    ps.FileCipher(inputfile, outputfile, password, work)


if __name__ == '__main__':
    main()
