Summary:	Tree compiler-compiler
Summary(pl):	Kompilator kompilacji drzew
Name:		treecc
Version:	0.2.2
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.southern-storm.com.au/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
URL:		http://www.southern-storm.com.au/treecc.html
BuildRequires:	autoconf
BuildRequires:	automake >= 1.6
BuildRequires:	gcc-c++
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The treecc program is designed to assist in the development of
compilers and other language-based tools. It manages the generation of
code to handle abstract syntax trees and operations upon the trees.

%description -l pl
Program treecc jest przeznaczony do pomocy w tworzeniu kompilatorów i
innych bazuj±cych na jêzykach narzêdzi. Zarz±dza generowaniem kodu do
obs³ugi abstrakcyjnej sk³adni drzew i operacji na drzewach.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
# %{_datadir}/treecc
%{_mandir}/man1/*
%{_infodir}/treecc*
