%define         _module docker-jenkins

%{!?svn_revision:%define svn_revision 1}

# COMPATIBILITY FIX: Jenkins job name is neccessary to make build root unique (for CentOS5 and earlier)
%{!?JOB_NAME:%define JOB_NAME standalone}

Name:           docker-jenkins
Version:        1.0
Release:        %{svn_revision}%{?dist}
Summary:        Docker container wrapper for Jenkins CI

Group:          Development/Tools
License:        GPLv3
URL:            http://jenkins.io/
Packager:       Roman Pavlyuk <roman.pavlyuk@gmail.com>
Source:         %{_module}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)-%{JOB_NAME}
BuildArch:      noarch

Requires:	docker

# Conflicts:	jenkins

%description
Jenkins CI Docker container control service for CentOS/Fedora Linux family

%define         pkg_user airvideo
%define         pkg_group %{pkg_user}

%prep
%setup -n %{_module}

%build
# Nothing to do

%install
# Create build directory
rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"

mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
cp -a src/*.service $RPM_BUILD_ROOT/%{_unitdir}

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{_module}
cp -a src/mounts.conf $RPM_BUILD_ROOT/%{_sysconfdir}/%{_module}

mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp -a src/docker-jenkins $RPM_BUILD_ROOT/%{_bindir}/docker-jenkins

%files
%doc

%config(noreplace) %{_sysconfdir}/%{_module}/mounts.conf

%attr(0755,root,root) %{_bindir}/docker-jenkins

%{_unitdir}/*.service

