#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Object-Signature
Version  : 1.08
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Object-Signature-1.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Object-Signature-1.08.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libo/libobject-signature-perl/libobject-signature-perl_1.07-2.debian.tar.xz
Summary  : 'Generate cryptographic signatures for objects'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Object-Signature-license = %{version}-%{release}
Requires: perl-Object-Signature-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Object-Signature,
version 1.08:
Generate cryptographic signatures for objects

%package dev
Summary: dev components for the perl-Object-Signature package.
Group: Development
Provides: perl-Object-Signature-devel = %{version}-%{release}
Requires: perl-Object-Signature = %{version}-%{release}

%description dev
dev components for the perl-Object-Signature package.


%package license
Summary: license components for the perl-Object-Signature package.
Group: Default

%description license
license components for the perl-Object-Signature package.


%package perl
Summary: perl components for the perl-Object-Signature package.
Group: Default
Requires: perl-Object-Signature = %{version}-%{release}

%description perl
perl components for the perl-Object-Signature package.


%prep
%setup -q -n Object-Signature-1.08
cd %{_builddir}
tar xf %{_sourcedir}/libobject-signature-perl_1.07-2.debian.tar.xz
cd %{_builddir}/Object-Signature-1.08
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Object-Signature-1.08/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Object-Signature
cp %{_builddir}/Object-Signature-1.08/LICENSE %{buildroot}/usr/share/package-licenses/perl-Object-Signature/b49005c259b7d098d7002eb25909e01a2f94426f
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Object::Signature.3
/usr/share/man/man3/Object::Signature::File.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Object-Signature/b49005c259b7d098d7002eb25909e01a2f94426f

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Object/Signature.pm
/usr/lib/perl5/vendor_perl/5.32.1/Object/Signature/File.pm
