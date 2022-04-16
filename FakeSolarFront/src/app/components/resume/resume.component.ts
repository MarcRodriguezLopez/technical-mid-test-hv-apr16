import { Component, OnInit } from '@angular/core';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-resume',
  templateUrl: './resume.component.html',
  styleUrls: ['./resume.component.css']
})
export class ResumeComponent implements OnInit {

  warnings: number = 0;
  criticals: number = 0;
  inspsWarnings: number = 0;
  inspsCriticals: number = 0;


  constructor( private dataService: DataService) { }

  ngOnInit(): void {

    this.dataService.getInspections()
      .subscribe( (inspections: any) => {
        for (let inspection of inspections) {
          this.warnings += inspection.issuesWarningCount
          this.criticals += inspection.issuesCriticalCount
          if (inspection.issuesCriticalCount > 0) {
            this.inspsCriticals += 1
          } else if (inspection.issuesWarningCount > 0) {
            this.inspsWarnings += 1
          }
        }
      })
      
  }

}
