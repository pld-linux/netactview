Summary:	Network connections viewer for Gnome
Summary(pl.UTF-8):	Przeglądarka połączeń sieciowych dla Gnome
Name:		netactview
Version:	0.6
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/netactview/%{name}-%{version}.tar.bz2
# Source0-md5:	8bc3e6f6e9e51e6546dd0985fdb11db0
Patch0:		%{name}-desktop.patch
URL:		http://netactview.sourceforge.net
BuildRequires:	GConf2-libs
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.8
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	libgnome-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
Requires:	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netactview is a graphical network connections viewer for Linux,
similar in functionality with Netstat. It includes features like host
name retrieval, automatic refresh and sorting.

%description -l pl.UTF-8
Netactview jest graficzną przeglądarką połączeń sieciowych dla
Linuksa, podobną w swojej funkcjonalności do Netstat. Posiada takie
cechy jak: odwzorowywanie nazw hostów, automatyczne odświeżanie i
sortowanie.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake} \
	--add-missing --gnu
%{__autoconf}

%configure \
	--enable-maintainer-mode

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/netactview
%{_desktopdir}/netactview.desktop
%{_mandir}/man1/netactview.1*
%{_datadir}/netactview
%{_pixmapsdir}/*.png
