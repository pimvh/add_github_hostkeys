import testinfra


def test_known_hosts(host):
    """test ssh ssh_known_hosts file has been created,
    with the requested key types"""

    assert host.file("/etc/ssh/ssh_known_hosts")

    for key in ["ssh-rsa", "ssh-ed25519", "ecdsa-sha2-nistp256"]:
        assert host.file("/etc/ssh/ssh_known_hosts").contains(f"github.com {key}")
