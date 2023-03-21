#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-cairosvg
Version  : 2.7.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/a8/e1/a69d14425d125fcac173c68b445816d3a539bb95a09edd620108bdc9348e/CairoSVG-2.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a8/e1/a69d14425d125fcac173c68b445816d3a539bb95a09edd620108bdc9348e/CairoSVG-2.7.0.tar.gz
Summary  : A Simple SVG Converter based on Cairo
Group    : Development/Tools
License  : LGPL-3.0 LGPL-3.0+
Requires: pypi-cairosvg-bin = %{version}-%{release}
Requires: pypi-cairosvg-license = %{version}-%{release}
Requires: pypi-cairosvg-python = %{version}-%{release}
Requires: pypi-cairosvg-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cairocffi)
BuildRequires : pypi(cssselect2)
BuildRequires : pypi(defusedxml)
BuildRequires : pypi(pillow)
BuildRequires : pypi(tinycss2)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
CairoSVG is an SVG converter based on Cairo. It can export SVG files to PDF,
EPS, PS, and PNG files.

%package bin
Summary: bin components for the pypi-cairosvg package.
Group: Binaries
Requires: pypi-cairosvg-license = %{version}-%{release}

%description bin
bin components for the pypi-cairosvg package.


%package license
Summary: license components for the pypi-cairosvg package.
Group: Default

%description license
license components for the pypi-cairosvg package.


%package python
Summary: python components for the pypi-cairosvg package.
Group: Default
Requires: pypi-cairosvg-python3 = %{version}-%{release}

%description python
python components for the pypi-cairosvg package.


%package python3
Summary: python3 components for the pypi-cairosvg package.
Group: Default
Requires: python3-core
Provides: pypi(cairosvg)
Requires: pypi(cairocffi)
Requires: pypi(cssselect2)
Requires: pypi(defusedxml)
Requires: pypi(pillow)
Requires: pypi(tinycss2)

%description python3
python3 components for the pypi-cairosvg package.


%prep
%setup -q -n CairoSVG-2.7.0
cd %{_builddir}/CairoSVG-2.7.0
pushd ..
cp -a CairoSVG-2.7.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679411457
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cairosvg
cp %{_builddir}/CairoSVG-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cairosvg/c09f9595f49b611cb4815dac18057910e5ff66b3 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cairosvg

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cairosvg/c09f9595f49b611cb4815dac18057910e5ff66b3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
