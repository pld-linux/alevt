Summary:	Teletext decoder and browser for the bttv based card
Summary(pl):	Dekoder Teletekstu
Summary(de):	Videotext/Teletext
Name:		alevt
Version:	1.6.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.goron.de/~froese/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-time-include.patch
Patch1:		%{name}-time.h.patch
URL:		http://www.goron.de/~froese/
BuildRequires:	XFree86-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
AleVT is a teletext/videotext decoder and browser for the bttv driver
(/dev/vbi) and X11. It features multiple windows, a page cache, regexp
searching, built-in manual, and more. There's also a program to get
the time from teletext and one to capture teletext pages from scripts.

%description -l pl
Dekoder oraz przegl±darka teletekstu. Pakiet ten umo¿liwia
przegl±danie stron telegazety.

%description -l de
X11 Videotextdecoder für den bttv Treiber.

%prep
%setup -q -n alevt-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install alevt alevt-date alevt-cap ${RPM_BUILD_ROOT}%{_bindir}
install {alevt-cap.1,alevt-date.1,alevt.1x} $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
