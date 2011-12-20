Summary:	Teletext decoder and browser for the bttv based card
Summary(de.UTF-8):	Videotext/Teletext
Summary(pl.UTF-8):	Dekoder Teletekstu
Name:		alevt
Version:	1.6.2
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://www.goron.de/~froese/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	e5a32776e7eff48ec48449b3c3c1cc23
Source1:	%{name}.desktop
Patch0:		%{name}-time-include.patch
Patch1:		%{name}-time.h.patch
URL:		http://www.goron.de/~froese/
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AleVT is a teletext/videotext decoder and browser for the bttv driver
(/dev/vbi) and X11. It features multiple windows, a page cache, regexp
searching, built-in manual, and more. There's also a program to get
the time from teletext and one to capture teletext pages from scripts.

%description -l pl.UTF-8
Dekoder oraz przeglądarka teletekstu. Pakiet ten umożliwia
przeglądanie stron telegazety.

%description -l de.UTF-8
X11 Videotextdecoder für den bttv Treiber.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_desktopdir},%{_pixmapsdir}}

install alevt alevt-date alevt-cap $RPM_BUILD_ROOT%{_bindir}
install alevt-cap.1 alevt-date.1 alevt.1x $RPM_BUILD_ROOT%{_mandir}/man1
install contrib/icon48x48.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.xpm
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_pixmapsdir}/%{name}.xpm
%{_desktopdir}/%{name}.desktop
