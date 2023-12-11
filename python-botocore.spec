%global pkgname botocore
%define buildid @BUILDID@

Name:           python-%{pkgname}
# NOTICE - Updating this package requires updating python-boto3
Version:        1.20.14
Release:        CROC35%{?buildid}%{?dist}
Summary:        Low-level, data-driven core of boto 3

License:        ASL 2.0
URL:            https://github.com/C2Devel/botocore.git
Source0:        https://pypi.io/packages/source/b/botocore/botocore-%{version}.tar.gz
BuildArch:      noarch

%description
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI as well as boto3.

%package -n     python%{python3_pkgversion}-%{pkgname}
Summary:        Low-level, data-driven core of boto 3
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-jmespath >= 0.7.1
Requires:       python%{python3_pkgversion}-dateutil >= 2.1
Requires:       python%{python3_pkgversion}-urllib3 >= 1.24.1

%description -n python%{python3_pkgversion}-%{pkgname}
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI as well as boto3.

%prep
%setup -q -n %{pkgname}-%{version}
rm -rf %{pkgname}.egg-info
# Remove online tests
rm -rf tests/integration

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pkgname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{pkgname}/
%{python3_sitelib}/%{pkgname}-*.egg-info/

%changelog
* Mon Dec 11 2023 Grigoriy Kulagin <grkulagin@croc.ru> - 1.20.14-CROC35
- autoscaling: Modify types for c2-client compatibility

* Tue Nov 07 2023 Linar Nasyyrov <lnasyyrov@croc.ru> - 1.20.14-CROC34
- s3: move trail recorc in s3 to system users
- paas: add elk and prometheus

* Tue Oct 10 2023 Grigoriy Kulagin <grkulagin@croc.ru> - 1.20.14-CROC33
- as: Make Notification Configurations C2-compliant
- ec2: add extra host fields
- ec2: make host properties instance family field list of string
- ec2: add host type api
- ec2: add supported instance types to host type

* Tue Sep 26 2023 Anastasia Berezko <aberezko@croc.ru> - 1.20.14-CROC32
- paas: add methods for databases and users

* Wed Aug 29 2023 Grigoriy Kulagin <grkulagin@croc.ru> - 1.20.14-CROC31
- eks: fix eks parameters for terraform

* Tue Jun 30 2023 Evgenii Proskurnev <eproskurnev@croc.ru> - 1.20.14-CROC30
- create EKS nodegroups and EKS clusters
- paas: change backupSettings startTime type

* Mon Jun 05 2023 Ivan Konov <ikonov@croc.ru> - 1.20.14-CROC29
- ec2: add SharedOwners option in TransitGateway

* Tue May 23 2023 Evgenii Proskurnev <eproskurnev@croc.ru> - 1.20.14-CROC28
- paas: add backup_expiration_days field and ModifyBackup method

* Wed Apr 26 2023 Andrey Kulaev <akulaev@croc.ru> - 1.20.14-CROC27
- add none validator
- paas: add paas client

* Fri Apr 07 2023 Ivan Konov <ikonov@croc.ru> - 1.20.14-CROC26
- backup: add IsConsistent flag
- backup: add NextExecutionDate field
- backup: add UpdateBackupSelection method

* Wed Mar 20 2023 Evgenii Proskurnev <eproskurnev@croc.ru> - 1.20.14-CROC25
- s3: rebase on S3 Api upstream
- eks: add method for toggling certificate autoupdate
- C2DEVEL-12500: add DeleteWorker request

* Wed Mar 1 2023 Grigoriy Kulagin <grkulagin@croc.ru> - 1.20.14-CROC24
- C2DEVEL-12315: Add field for certificates auto-update

* Wed Jan 23 2023 Andrey Kulaev <akulaev@croc.ru> - 1.20.14-CROC23
- spec: add support for koji 8.4

* Mon Dec 19 2022 Andrey Kulaev <akulaev@croc.ru> - 1.20.14-CROC22
- ec2: add fields VolumeSizeInBytes and SizeInBytes

* Mon Dec 12 2022 Anastasia Berezko <aberezko@croc.ru> - 1.20.14-CROC21
- ec2: sync API with c2

* Wed Nov 30 2022 Anastasia Berezko <aberezko@croc.ru> - 1.20.14-CROC20
- C2DEVEL-11786: Return DesiredCapacity after policy execution
- ec2: sync API with c2

* Tue Nov 3 2022 Andrey Kulaev <akulaev@croc.ru> - 1.20.14-CROC19
- ec2: update params DescribeAccountAttributes

* Wed Oct 12 2022 Alexander Chernev <achernev@croc.ru> - 1.20.14-CROC18
- add aws_sudo_id to json based services (EKS)

* Thu Jul 14 2022 Andrey Kulaev <akulaev@croc.ru> - 1.20.14-CROC17
- ec2: add ReplacePrimaryNetworkInterface method

* Wed Jun 22 2022 Evgeny Kovalev <evgkovalev@croc.ru> - 1.20.14-CROC16
- ec2: add VirtualizationType,HighAvailable to LaunchTemplateData

* Wed Jun 01 2022 Andrey Kulaev <akulaev@croc.ru> - 1.20.14-CROC15
- ec2: add HighAvailable,VirtualizationType,KeyName to InstanceAttribute
- ec2: add highAvailable,virtualizationType,keyName to InstanceAttributeName
- ec2: add RootDeviceName,HighAvailable,VirtualizationType,KeyName to ModifyInstanceAttributeRequest

* Fri May 27 2022 Ivan Konov <ikonov@croc.ru> - 1.20.14-CROC14
- ec2: add Switch and change Instance methods

* Tue May 17 2022 Andrey Kulaev <akulaev@croc.ru> - 1.20.14-CROC13
- ec2: add volume version ID to CreateSnapshotRequest

* Wed Apr 06 2022 Ivan Konov <ikonov@croc.ru> - 1.20.14-CROC12
- autoscaling: Modify types for c2-client compat
- spec: fix correct provides for requires in gear

* Tue Mar 01 2022 Ivan Konov <ikonov@croc.ru> - 1.20.14-CROC11
- ec2: add Description to ModifySnapshotAttributeRequest

* Mon Feb 07 2022 Alexander Chernev <achernev@croc.ru> - 1.20.14-CROC10
- Technical Release

* Mon Feb 07 2022 Alexander Chernev <achernev@croc.ru> - 1.20.14-CROC9
- botocore: data: ec2: add CreateVolumeExportTask method
- botocore: data: ec2: add DescribeExportVolumeTasks method
- botocore: data: ec2: add Notify and Email fields to IE requests
- botocore: data: ec2: add Progress field to ExportTask structure
- eks: change requestUri of ModifyWorkersInstanceType method
- botocore: data: ec2: add VirtualizationType to ImportImage request
- botocore: data: ec2: add ImageName, Notify, Email to ImportImage request
- ec2: add volume versions

* Mon Nov 29 2021 Konstantin Zakharov <kzakharov@croc.ru> - 1.20.14-CROC8
- spec: revert build for py2
- eks: add ModifyWorkersInstanceType operations

* Wed Nov 24 2021 Evgeny Kovalev <evgkovalev@croc.ru> - 1.20.14-CROC7
- eks: add ModifyUserData operations

* Tue Oct 26 2021 Alex Rudenko <arudenko@croc.ru> - 1.20.14-CROC6
- spec: add urllib3 1.25.6 to dependencies
- spec: remove build for py2

* Wed Oct 20 2021 Andrey Kulaev <akulaev@croc.ru> - 1.20.14-CROC5
- eks: use an already allocated public ip address
- eks: show EbsUser field
- eks: add Pod and Service Subnet CIDR to cluster model

* Mon Aug 23 2021 Andrey Kulaev <akulaev@croc.ru> - 1.20.14-CROC4
- eks: deploying a high availability cluster in multiple AZ
- eks: add ModifySecurityGroups operations
- eks: add shapes Instance and InstanceList
- eks: use SecurityGroupIds instead of SecurityGroups

* Fri Jul 02 2021 Andrey Kulaev <akulaev@croc.ru> - 1.20.14-CROC3
- eks: fix shape name typo Bool -> Boolean

* Mon Jun 28 2021 Max Kotov <makotov@croc.ru> - 1.20.14-CROC2
- Introduce KS Public API

* Wed Feb 24 2021 Alexander Chernev <achernev@croc.ru> - 1.20.14-CROC1
- Update to latest botocore - 1.20.14
