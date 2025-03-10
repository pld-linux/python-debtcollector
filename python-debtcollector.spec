#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (missing deps)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	A collection of Python deprecation patterns and strategies that help you collect your technical debt in a non-destructive manner
Summary(pl.UTF-8):	Zbiór wzorców i strategii odchodzenia, pozwalający gromadzić dług technologiczny w sposób niedestruktywny
Name:		python-debtcollector
# keep 1.x here for python2 support
Version:	1.22.0
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/d/debtcollector/debtcollector-%{version}.tar.gz
# Source0-md5:	0d12694a93a16824b1c67bece341229e
URL:		https://pypi.org/project/debtcollector/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr >= 3.0.0
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-fixtures >= 3.0.0
BuildRequires:	python-funcsigs >= 1.0.0
BuildRequires:	python-six >= 1.10.0
BuildRequires:	python-stestr >= 2.0.0
BuildRequires:	python-subunit >= 1.0.0
BuildRequires:	python-testtools >= 2.2.0
BuildRequires:	python-wrapt >= 1.7.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-pbr >= 3.0.0
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-fixtures >= 3.0.0
BuildRequires:	python3-funcsigs >= 1.0.0
BuildRequires:	python3-six >= 1.10.0
BuildRequires:	python3-stestr >= 2.0.0
BuildRequires:	python3-subunit >= 1.0.0
BuildRequires:	python3-testtools >= 2.2.0
BuildRequires:	python3-wrapt >= 1.7.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-openstackdocstheme >= 1.18.1
BuildRequires:	python-reno >= 2.5.0
BuildRequires:	sphinx-pdg-2 >= 1.7.0
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of Python deprecation patterns and strategies that help
you collect your technical debt in a non-destructive manner. The goal
of this library is to provide well documented developer facing
deprecation patterns that start of with a basic set and can expand
into a larger set of patterns as time goes on. The desired output of
these patterns is to apply the warnings module to emit
DeprecationWarning or PendingDeprecationWarning or similar derivative
to developers using libraries (or potentially applications) about
future deprecations.

%description -l pl.UTF-8
Zbiór wzorców i strategii odchodzenia, pozwalający gromadzić dług
technologiczny w sposób niedestruktywny. Celem biblioteki jest
dostarczenie dobrze udokumentowanych, wychodzących naprzeciw
programistom wzorców odchodzenia, które zaczynają się od podstawowego
zbioru i mogą rozszerzać do większego zbioru wzorców w miarę upływu
czasu. Pożądanym wyjściem wzorców jest wykorzystanie modułu warnings
do emitowania wyjątków DeprecationWarning, PendingDeprecationWarning
lub pochodnych programistom wykorzystującym biblioteki (ew. aplikacje)
o przyszłych odchodzących funkcjach.

%package -n python3-debtcollector
Summary:	A collection of Python deprecation patterns and strategies that help you collect your technical debt in a non-destructive manner
Summary(pl.UTF-8):	Zbiór wzorców i strategii odchodzenia, pozwalający gromadzić dług technologiczny w sposób niedestruktywny
Group:		Libraries/Python

%description -n python3-debtcollector
A collection of Python deprecation patterns and strategies that help
you collect your technical debt in a non-destructive manner. The goal
of this library is to provide well documented developer facing
deprecation patterns that start of with a basic set and can expand
into a larger set of patterns as time goes on. The desired output of
these patterns is to apply the warnings module to emit
DeprecationWarning or PendingDeprecationWarning or similar derivative
to developers using libraries (or potentially applications) about
future deprecations.

%description -n python3-debtcollector -l pl.UTF-8
Zbiór wzorców i strategii odchodzenia, pozwalający gromadzić dług
technologiczny w sposób niedestruktywny. Celem biblioteki jest
dostarczenie dobrze udokumentowanych, wychodzących naprzeciw
programistom wzorców odchodzenia, które zaczynają się od podstawowego
zbioru i mogą rozszerzać do większego zbioru wzorców w miarę upływu
czasu. Pożądanym wyjściem wzorców jest wykorzystanie modułu warnings
do emitowania wyjątków DeprecationWarning, PendingDeprecationWarning
lub pochodnych programistom wykorzystującym biblioteki (ew. aplikacje)
o przyszłych odchodzących funkcjach.

%package apidocs
Summary:	API documentation for Python debtcollector module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona debtcollector
Group:		Documentation

%description apidocs
API documentation for Pythona debtcollector module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona debtcollector.

%prep
%setup -q -n debtcollector-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
sphinx-build-2 -b html doc/source doc/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/debtcollector/tests
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/debtcollector/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/debtcollector
%{py_sitescriptdir}/debtcollector-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-debtcollector
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/debtcollector
%{py3_sitescriptdir}/debtcollector-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_modules,_static,contributor,install,reference,user,*.html,*.js}
%endif
