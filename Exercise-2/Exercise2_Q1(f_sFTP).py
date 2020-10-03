#import  pysftp

import pysftp

with pysftp.Connection('hostname', username='me', password='secret') as sftp:

    with sftp.cd('/allcode'):           # temporarily chdir to allcode
        sftp.put('/pycode/filename')  	# upload file to allcode/pycode on remote
        sftp.get('remote_file')  
