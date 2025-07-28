# X.org drivers use symbols from the X server
%global _disable_ld_no_undefined 1
#define snapshot 20181023

Summary:	X.org driver for Intel graphics controllers
Name:		x11-driver-video-intel
Version:	3.0.0.1%{?snapshot:~%{snapshot}}
Group:		System/X11
License:	MIT
URL:		https://xorg.freedesktop.org
Release:        1
%if 0%{?snapshot:1}
Source0:        xf86-video-intel-%{snapshot}.tar.bz2
%else
Source0:	https://github.com/X11Libre/xf86-video-intel/archive/refs/tags/xlibre-xf86-video-intel-%{version}.tar.gz
%endif
# Mandriva patches
Patch100:	0100-Mandriva-fix-check-vt-switch.patch
# (cg) Disable for now as it hits an assert on Xserver 1.9
#Patch101: 0101-fix-NoneBG-support.patch
# Upstream patches

BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(udev) >= 186
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server) >= 1.18
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xvmc)
# For intel-virtual-output
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(xfont)
BuildRequires:	pkgconfig(xcb-dri3)
BuildRequires:	pkgconfig(xcb-sync)
BuildRequires:	pkgconfig(x11-xcb)
BuildRequires:	pkgconfig(xshmfence)
BuildRequires:  valgrind
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)
Requires:	udev

Conflicts:	xorg-x11-server < 7.0
Obsoletes:	x11-driver-video-intel13 <= 1.9.94
Obsoletes:	x11-driver-video-i810
Obsoletes:	x11-driver-video-i810-downscaling
Obsoletes:	x11-driver-video-intel-fast-i830
# (tpg) this is needed to get vaapi works out of box
Requires:	libva-intel-driver
Requires:	%{_lib}dri-drivers-intel

BuildSystem:	meson

%patchlist
#intel-3.0.0.1-compile.patch

%description
x11-driver-video-intel is the X.org driver for Intel video chipsets.

%files
%{_bindir}/intel-virtual-output
%{_libdir}/libIntelXvMC.so*
%{_libdir}/libI810XvMC.so*
%{_mandir}/man4/intel.4*
%{_mandir}/man4/intel-virtual-output.4*
%{_libexecdir}/xf86-video-intel-backlight-helper
%{_datadir}/polkit-1/actions/org.x.xf86-video-intel.backlight-helper.policy
%{_libdir}/xorg/modules/drivers/intel_drv.so
