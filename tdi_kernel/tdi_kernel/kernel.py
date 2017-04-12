from ipykernel.kernelbase import Kernel
from MDSplus import Data

class TdiKernel(Kernel):
    implementation = 'Tdi'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {
        'name': 'tdi expressions',
        'mimetype': 'text/plain',
        'file_extension': '.tdi',
    }
    banner = "MDSplus TDI kernel - expression evaluation"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            try:
                ans = Data.execute(code)
                stream_content = {'name': 'stdout', 'text': str(ans)}
            except Exception as e:
                stream_content = {'name': 'stderr', 'text': str(e)}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
