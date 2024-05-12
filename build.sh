TERMUX_PKG_HOMEPAGE=https://github.com/Intikam21kurucu/intframework
TERMUX_PKG_DESCRIPTION="Ağ güvenliği ve siber istihbarat toplama aracı."
TERMUX_PKG_LICENSE="GPL"
TERMUX_PKG_MAINTAINER="[Your Name] <[Your Email]>"
TERMUX_PKG_VERSION=1.0
TERMUX_PKG_SRCURL=https://github.com/Intikam21kurucu/intframework/archive/refs/tags/v$TERMUX_PKG_VERSION.tar.gz
TERMUX_PKG_SHA256=SKIP
TERMUX_PKG_DEPENDS="python, python-requests, python-scrapy"

termux_step_make() {
  python setup.py build
}

termux_step_make_install() {
  python setup.py install --prefix=$TERMUX_PREFIX --force
}
