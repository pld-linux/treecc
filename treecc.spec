Summary:	Tree compiler-compiler
Summary(pl.UTF-8):	Kompilator kompilacji drzew
Summary(pt_BR.UTF-8):	Tree Compilador de compiladores
Name:		treecc
Version:	0.3.8
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.southern-storm.com.au/download/%{name}-%{version}.tar.gz
# Source0-md5:	ca26c97d00cff28fa312155b2228ff97
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

%description -l pl.UTF-8
Program treecc jest przeznaczony do pomocy w tworzeniu kompilatorów i
innych bazujących na językach narzędzi. Zarządza generowaniem kodu do
obsługi abstrakcyjnej składni drzew i operacji na drzewach.

%description -l pt_BR.UTF-8
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

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc README NEWS ChangeLog AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%{_infodir}/treecc*
