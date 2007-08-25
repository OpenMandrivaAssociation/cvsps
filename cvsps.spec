Name:           cvsps
Version:        2.1
Release:        %mkrel 3
Summary:        Patchset tool for CVS

Group:          Development/Other
License:        GPL
URL:            http://www.cobite.com/cvsps/
Source0:        http://www.cobite.com/cvsps/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  zlib-devel
# Requires cvs only with --no-cvs-direct, but I cannot imagine this dep
# being a problem on systems where cvsps will be installed...
Requires:       cvs

%description
CVSps is a program for generating 'patchset' information from a CVS
repository.  A patchset in this case is defined as a set of changes
made to a collection of files, and all committed at the same time
(using a single 'cvs commit' command).  This information is valuable
to seeing the big picture of the evolution of a cvs project.  While
cvs tracks revision information, it is often difficult to see what
changes were committed 'atomically' to the repository.


%prep
%setup -q


%build
CFLAGS="$RPM_OPT_FLAGS" %make


%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 cvsps $RPM_BUILD_ROOT%{_bindir}/cvsps
install -Dpm 644 cvsps.1 $RPM_BUILD_ROOT%{_mandir}/man1/cvsps.1


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CHANGELOG COPYING README merge_utils.sh
%{_bindir}/cvsps
%{_mandir}/man1/cvsps.1*



