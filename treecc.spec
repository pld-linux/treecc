#
# Conditional build:
%bcond_without	tests	# "make check"
#
Summary:	Tree compiler-compiler
Summary(pl.UTF-8):	Kompilator kompilacji drzew
Summary(pt_BR.UTF-8):	Tree Compilador de compiladores
Name:		treecc
Version:	0.3.10
Release:	2
License:	GPL v2+
Group:		Development/Languages
Source0:	http://download.savannah.gnu.org/releases/dotgnu-pnet/%{name}-%{version}.tar.gz
# Source0-md5:	def09f2132f87d6a38a0718e2f14ee61
URL:		http://www.gnu.org/software/dotgnu/pnet.html
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
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%if %{with tests}
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# API not exported (should be noinst)
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libtreecc.a

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/{binary_readme,extending}.txt doc/essay.html
%attr(755,root,root) %{_bindir}/treecc
%{_mandir}/man1/treecc.1*
%{_infodir}/treecc.info*
