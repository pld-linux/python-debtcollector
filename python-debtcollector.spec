#
# Conditional build:
%bcond_with	doc	# do build doc (missing deps)
%bcond_with	tests	# do perform "make test" (missing deps)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	A collection of Python deprecation patterns and strategies that help you collect your technical debt in a non-destructive manner
Name:		python-debtcollector
Version:	1.17.0
Release:	5
License:	Apache
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/d/debtcollector/debtcollector-%{version}.tar.gz
# Source0-md5:	f9d8b024ca72cf50505a48f4691fcdc3
URL:		https://pypi.python.org/pypi/debtcollector
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%endif
Requires:	python-funcsigs >= 0.4
Requires:	python-pbr >= 2.0.0
Requires:	python-six >= 1.9.0
Requires:	python-wrapt >= 1.7.0
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

%package -n python3-debtcollector
Summary:	A collection of Python deprecation patterns and strategies that help you collect your technical debt in a non-destructive manner
Group:		Libraries/Python
Requires:	python3-pbr >= 2.0.0
Requires:	python3-six >= 1.9.0
Requires:	python3-wrapt >= 1.7.0

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
cd doc
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install

# python dependency generator does not support conditionals
# remove python2-only dependencies here
sed -i -e"/python_version=='2./,+1 d" $RPM_BUILD_ROOT%{py3_sitescriptdir}/debtcollector-%{version}-py*.egg-info/requires.txt
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
%doc doc/_build/html/*
%endif
