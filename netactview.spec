Summary:	Network connections viewer for Gnome
Summary(pl.UTF-8):	Przeglądarka połączeń sieciowych dla Gnome
Name:		netactview
Version:	0.4.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/netactview/%{name}-%{version}.tar.bz2
# Source0-md5:	ffe73b1978c83415fef1cd0bcbec97c1
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

%clean
rm -rf $RPM_BUILD_ROOT

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

%files
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/netactview
%{_desktopdir}/netactview.desktop
%{_mandir}/man1/netactview.1*
%{_datadir}/locale
%{_datadir}/netactview
%{_pixmapsdir}
