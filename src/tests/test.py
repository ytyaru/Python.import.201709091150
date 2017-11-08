#ひとつ上の階層における全ディレクトリをimportディレクトリに追加する
import sys, os
rootdir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
for root, dirs, files in os.walk(rootdir):
    for d in dirs:
        print(os.path.join(root, d))
        sys.path.append(os.path.join(root, d))

import mymodule
#import mypackage.mymodule
mymodule.mymethod()
