%define module	Net-XMPP
%define name	perl-%{module}
%define version 1.0
%define rel	2

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
Summary:	XMPP Perl Library
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Net::XMPP is a convenient tool to use for any perl script that would
like to utilize the XMPP Instant Messaging protocol.  While not a
client in and of itself, it provides all of the necessary back-end
functions to make a CGI client or command-line perl client feasible 
and easy to use.  Net::XMPP is a wrapper around the rest of the
official Net::XMPP::xxxxxx packages.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
#make test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/Net
%{_mandir}/*/*

