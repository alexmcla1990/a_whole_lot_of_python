using System;
using System.ComponentModel;
using EmployeeManager.Common.DataProvider;
using EmployeeManager.Common.Model;



namespace EmployeeManager.ViewModel
{
    public class EmployeeViewModel : ViewModelBase
    {
        public EmployeeViewModel(Employee employee, IEmployeeDataProvider employeeDataProvider)
        {
            _employee = employee;
            EmployeeDataProvider = employeeDataProvider;
        }
        public string FirstName {
            get { return _employee.FirstName; }
            set {
                if (_employee.FirstName != value) {
                    _employee.FirstName = value;
                    RaisePropertyChanged(nameof(FirstName));
                    RaisePropertyChanged(nameof(CanSave));



                }
            
            
            }
        }

        public DateTimeOffset EntryDate
        {
            get { return _employee.EntryDate; }
            set
            {
                if (_employee.EntryDate != value)
                {
                    _employee.EntryDate = value;
                    RaisePropertyChanged(nameof(EntryDate));



                }


            }
        }

        public int JobRoleId
        {
            get { return _employee.JobRoleId; }
            set
            {
                if (_employee.JobRoleId != value)
                {
                    _employee.JobRoleId = value;
                    RaisePropertyChanged(nameof(JobRoleId));



                }


            }
        }

        public bool IsCoffeeDrinker
        {
            get { return _employee.IsCoffeeDrinker; }
            set
            {
                if (_employee.IsCoffeeDrinker != value)
                {
                    _employee.IsCoffeeDrinker = value;
                    RaisePropertyChanged(nameof(IsCoffeeDrinker));



                }


            }
        }
        public bool CanSave => !string.IsNullOrEmpty(FirstName);
        public void Save() { 
        EmployeeDataProvider.SaveEmployee(_employee);
        
        
        }
        public Employee _employee { get; }
        public IEmployeeDataProvider EmployeeDataProvider { get; }

       
    }
}