from threading import Lock, Thread
import ctypes
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


BLOCKING_AT_LOOPBACK_INTERFACE = False


def is_running_as_admin():
    try:
        return bool(ctypes.windll.shell32.IsUserAnAdmin())
    except OSError:
        return False


class ProcessHostsFile:
    def __init__(self):
        self.hosts_file_path = r"C:\Windows\System32\drivers\etc\hosts"
        self.hosts_fd = None
        self.hosts_content = ""
        self.hosts_content_lines = []
        self.lock = Lock()
        self._read_hosts_file()

    def _open_hosts_file(self, mode="r+"):
        self.hosts_fd = open(self.hosts_file_path, mode, encoding="utf-8")

    def _read_hosts_file(self):
        with self.lock:
            try:
                with open(self.hosts_file_path, "r", encoding="utf-8") as f:
                    self.hosts_content_lines = f.readlines()
                    self.hosts_content = "".join(self.hosts_content_lines)
            except OSError as exc:
                raise Exception(
                    "Hosts file is not readable. Please run the app as an administrator."
                ) from exc

    def append_to_hosts_file(self, data):
        with self.lock:
            self._open_hosts_file()
            try:
                if self.hosts_content and not self.hosts_content.endswith("\n"):
                    self.hosts_content += "\n"
                self.hosts_content += data.rstrip() + "\n"
                self._write_hosts_file()
                self.hosts_content_lines = self.hosts_content.splitlines(keepends=True)
            finally:
                self._close_hosts_file()

    def remove_tag_hosts_file(self, tag_start, tag_end):
        with self.lock:
            new_lines = []
            in_tag = False
            for line in self.hosts_content_lines:
                stripped = line.strip()
                if stripped == tag_start:
                    in_tag = True
                    continue
                if stripped == tag_end:
                    in_tag = False
                    continue
                if not in_tag:
                    new_lines.append(line)

            self.hosts_content_lines = new_lines
            self.hosts_content = "".join(new_lines)
            try:
                with open(self.hosts_file_path, "w", encoding="utf-8") as f:
                    f.writelines(new_lines)
            except OSError as exc:
                raise Exception("Error writing to hosts file.") from exc

    def _write_hosts_file(self):
        self.hosts_fd.seek(0)
        self.hosts_fd.write(self.hosts_content)
        self.hosts_fd.truncate()

    def _close_hosts_file(self):
        if self.hosts_fd:
            self.hosts_fd.close()
            self.hosts_fd = None


class AdobeUpdateServiceBlocker:
    USER_AGENT = "MUCH-THANKS/1.1 @v0id_user"
    BLOCK_127_ADOBE_HOSTS_ENDPOINT = "https://a.dove.isdumb.one/127.txt"
    BLOCK_0000_ADOBE_HOSTS_ENDPOINT = "https://a.dove.isdumb.one/list.txt"
    BLOCK_TAG_127_START = "# Start Blocking Adobe At 127.0.0.1"
    BLOCK_TAG_127_END = "# End Blocking Adobe At 127.0.0.1"
    BLOCK_TAG_0000_START = "# Start Blocking Adobe At 0.0.0.0"
    BLOCK_TAG_0000_END = "# End Blocking Adobe At 0.0.0.0"

    def __init__(self):
        self.process_hosts_file = ProcessHostsFile()

    def _fetch_block_list(self, url):
        request = Request(url, headers={"User-Agent": self.USER_AGENT})
        try:
            with urlopen(request, timeout=15) as response:
                return response.read().decode("utf-8")
        except HTTPError as exc:
            raise RuntimeError(f"Failed to download block list: HTTP {exc.code}") from exc
        except URLError as exc:
            raise RuntimeError(f"Failed to download block list: {exc.reason}") from exc

    def blocking_at_loopback_interface(self):
        block_list = self._fetch_block_list(self.BLOCK_127_ADOBE_HOSTS_ENDPOINT)
        hosts_block_list = (
            f"{self.BLOCK_TAG_127_START}\n{block_list.rstrip()}\n{self.BLOCK_TAG_127_END}"
        )
        self.process_hosts_file.append_to_hosts_file(hosts_block_list)

    def blocking_at_service_interface(self):
        block_list = self._fetch_block_list(self.BLOCK_0000_ADOBE_HOSTS_ENDPOINT)
        hosts_block_list = (
            f"{self.BLOCK_TAG_0000_START}\n{block_list.rstrip()}\n{self.BLOCK_TAG_0000_END}"
        )
        self.process_hosts_file.append_to_hosts_file(hosts_block_list)

    def hosts_file_clean(self):
        self.process_hosts_file._read_hosts_file()
        self.process_hosts_file.remove_tag_hosts_file(
            self.BLOCK_TAG_0000_START, self.BLOCK_TAG_0000_END
        )
        self.process_hosts_file.remove_tag_hosts_file(
            self.BLOCK_TAG_127_START, self.BLOCK_TAG_127_END
        )

    def start_block_service(self):
        threads = []
        if BLOCKING_AT_LOOPBACK_INTERFACE:
            threads.append(Thread(target=self.blocking_at_loopback_interface))
        threads.append(Thread(target=self.blocking_at_service_interface))
        self.hosts_file_clean()

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()


def main():
    print("Please pay attention...")

    if not is_running_as_admin():
        input("You should run this script as an administrator.")
        raise SystemExit(1)

    AdobeUpdateServiceBlocker().start_block_service()
    input("Ok you can close the script now...\nRun it again if the popup appears later...")


if __name__ == "__main__":
    main()
