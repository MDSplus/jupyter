from ipykernel.kernelbase import Kernel
from MDSplus import Data

class MdstclKernel(Kernel):
    implementation = 'Mdstcl'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {
        'name': 'mdstcl commands',
        'mimetype': 'text/plain',
        'file_extension': '.tcl',
    }
    banner = "MDSplus Mdstcl kernel - Tree Command Language interpreter"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            try:
                lines=code.split('\n')
                for line in lines:
                  ans = Data.execute('_status=tcl($1,_out),_out',line)
                  status = int(Data.execute('_status'))
                  if status & 1:
                     stream_content = {'name': 'stdout', 'text': str(ans)}
                  else:
                    stream_content = {'name':'stderr','text': '\n'.join([line,str(ans)])}
                  self.send_response(self.iopub_socket,'stream',stream_content)
            except Exception as e:
                stream_content = {'name': 'stderr', 'text': str(e)}
                self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
