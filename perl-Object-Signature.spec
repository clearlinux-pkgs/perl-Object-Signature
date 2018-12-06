#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Object-Signature
Version  : 1.08
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Object-Signature-1.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Object-Signature-1.08.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libo/libobject-signature-perl/libobject-signature-perl_1.07-2.debian.tar.xz
Summary  : 'Generate cryptographic signatures for objects'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Object-Signature,
version 1.08:
Generate cryptographic signatures for objects

%package dev
Summary: dev components for the perl-Object-Signature package.
Group: Development
Provides: perl-Object-Signature-devel = %{version}-%{release}

%description dev
dev components for the perl-Object-Signature package.


%prep
%setup -q -n Object-Signature-1.08
cd ..
%setup -q -T -D -n Object-Signature-1.08 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Object-Signature-1.08/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
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
/usr/lib/perl5/vendor_perl/5.28.1Object/Signature.pm
/usr/lib/perl5/vendor_perl/5.28.1Object/Signature/File.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Object::Signature.3
/usr/share/man/man3/Object::Signature::File.3
