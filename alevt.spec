Summary: Videotext/Teletext 
Summary(pl): Videotext/Teletext
Summary(de): Videotext/Teletext
Name: alevt
Version: 1.5.1
Release: 1
Copyright: GNU
Group: X11/Applications
Group(pl): X11/Aplikacje
Source: http://user.exit.de/froese/%{name}/%{name}-%{version}.tar.gz
URL: http://user.exit.de/froese
BuildRequires:  XFree86-devel
BuildRequires:	libpng
BuildRequires:	zlib-devel
BuildRoot:      /tmp/%{name}-%{version}-root


%description
Teletext decoder and browser for the bttv driver.
If you have an older bttv < v0.5.20 or the one contained in the 2.2.x
kernels you should supply the -oldbttv option.


%description -l pl
Dekoder 
Je¶li u¿ywasz starszego bttv ni¿ v0.5.20 lub driverów zawieraj±cych siê w 
kernelu 2.2.x powiniene¶ u¿yæ opcji -oldbttv

%description -l de
X11 Videotextdecoder für den bttv Treiber.
Für die alte bttv-Version (<v0.5.20) der 2.2-er Kernel sollte der
Parameter -oldbttv verwendet werden.


%prep
%setup -q -n alevt-%{version}

%build
make FONT=latin-2

%install

rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -s {alevt,alevt-date,alevt-cap} ${RPM_BUILD_ROOT}%{_bindir}
install {alevt-cap.1,alevt-date.1,alevt.1x} $RPM_BUILD_ROOT%{_mandir}/man1
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* README CHANGELOG COPYRIGHT

%clean
rm -rf $RPM_BUILD_ROOT

%files

%defattr(644,root,root,755)
%doc {README,CHANGELOG,COPYRIGHT}.gz

%attr(755,root,root) %{_bindir}/alevt
%attr(755,root,root) %{_bindir}/alevt-date
%attr(755,root,root) %{_bindir}/alevt-cap

%{_mandir}/man1/alevt-cap.1.*
%{_mandir}/man1/alevt-date.1.*
%{_mandir}/man1/alevt.1x.*
