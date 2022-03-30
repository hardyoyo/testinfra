import glob
import os

workspace = os.environ['WORKSPACE']
lando_key_name = os.environ['LANDO_KEY_NAME']

jschol_wip_paths = glob.glob(workspace + "/jschol-wip*")

def test_lando_local_file(host):
    for path in jschol_wip_paths:
        wip_path = host.file(path)
        assert wip_path.exists
        assert wip_path.is_directory
        lando_local_file = host.file(path + "/.lando.local.yml")
        assert lando_local_file.exists
        assert lando_local_file.is_file
        assert lando_local_file.contains("keys:\n  - " + lando_key_name )

def test_lando_local_env(host):
    for path in jschol_wip_paths:
        lando_local_env = host.file(path + "/local.env")
        assert lando_local_env.exists
        assert lando_local_env.is_file
        assert lando_local_env.contains("SOCKS_KEYPATH=/user/.ssh/" + lando_key_name )

