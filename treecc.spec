Summary:	Tree compiler-compiler
Summary(pl):	Kompilator kompilacji drzew
Summary(pt_BR):	Tree Compilador de compiladores
Name:		treecc
Version:	0.3.6
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.southern-storm.com.au/download/%{name}-%{version}.tar.gz
# Source0-md5:	56426279e6017af909353176e582fb28
URL:		http://www.southern-storm.com.au/treecc.html
BuildRequires:	autoconf
BuildRequires:	automake >= 1.6
BuildRequires:	bison
BuildRequires:	flex
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

%description -l pt_BR
O programa treecc é destinado a auxiliar no desenvolviemnto de
compiladores e outras ferramentas baseadas em linguagens. Ele controla
a geração de código para manipulação de árvores de sintaxe abstrata e
operações através de árvores

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}
%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README NEWS ChangeLog AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%{_infodir}/treecc*
