using EmployeeManager.Common.DataProvider;
using EmployeeManager.Common.Model;
using System.Collections.ObjectModel;

namespace EmployeeManager.ViewModel
{
  public class MainViewModel : ViewModelBase
  {
    private EmployeeViewModel _selectedEmployee;
    private readonly IEmployeeDataProvider _employeeDataProvider;

    public MainViewModel(IEmployeeDataProvider employeeDataProvider)
    {
      _employeeDataProvider = employeeDataProvider;
    }

    public ObservableCollection<EmployeeViewModel> Employees { get; } = new();
    public ObservableCollection<JobRole> JobRoles { get; } = new();

    public EmployeeViewModel SelectedEmployee
    {
      get => _selectedEmployee;
      set
      {
        if (_selectedEmployee != value)
        {
          _selectedEmployee = value;
          RaisePropertyChanged();
          RaisePropertyChanged(nameof(IsEmployeeSelected));
        }
      }
    }

    public bool IsEmployeeSelected => SelectedEmployee != null;

    public void Load()
    {
      var employees = _employeeDataProvider.LoadEmployees();
      var jobRoles = _employeeDataProvider.LoadJobRoles();

      Employees.Clear();
      foreach (var employee in employees)
      {
        Employees.Add(new EmployeeViewModel(employee, _employeeDataProvider));
      }

      JobRoles.Clear();
      foreach (var jobRole in jobRoles)
      {
        JobRoles.Add(jobRole);
      }
    }

  }
}
