%define module	Net-XMPP

Summary:	XMPP Perl Library
Name:		perl-%{module}
Version:	1.02
Release:	13
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(XML::Stream)

%description
Net::XMPP is a convenient tool to use for any perl script that would
like to utilize the XMPP Instant Messaging protocol.  While not a
client in and of itself, it provides all of the necessary back-end
functions to make a CGI client or command-line perl client feasible 
and easy to use.  Net::XMPP is a wrapper around the rest of the
official Net::XMPP::xxxxxx packages.

%prep
%setup -qn %{module}-%{version}

%build
%__perl Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc CHANGES README
%{perl_vendorlib}/Net
%{_mandir}/man3/*

