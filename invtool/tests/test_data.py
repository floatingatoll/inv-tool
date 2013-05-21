from gettext import gettext as _
import random
import time
import string
random.seed(time.time())
N = 32
TEST_DOMAIN = _(
    ''.join(random.choice(string.ascii_uppercase + string.digits)
            for x in range(N)) + ".foo.bar.test_domain.lab1.mozilla.net"
)
TEST_FQDN = "testfqdn." + TEST_DOMAIN
TEST_IPv4 = lambda: "10.1.2." + str(random.randint(0, 255))
TEST_IPv6 = lambda: "1234:1234::1" + str(random.randint(0, 255))
TEST_DESCRIPTION = '"This is a description"'
TEST_TTL = "9999"
TEST_PORT = "8888"
TEST_WEIGHT = "7777"
TEST_PRIORITY = "5555"
TEST_TEXT = "FOO 'BAR' baz"
TEST_INAME = lambda: "eth" + str(random.randint(0, 255))
