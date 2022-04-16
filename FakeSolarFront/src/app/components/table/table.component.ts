import { Component, OnInit } from '@angular/core';
import { DataService } from '../../services/data.service';

interface INSPECTIONS {
  title: String,
  inspectorName: String,
  itemsOk: Number,
  issuesWarningCount: Number,
  issuesCriticalCount: Number,
  company: String,
  color: any
}

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent implements OnInit {

  insps: INSPECTIONS[] = [];

  constructor( private dataService: DataService) { }

  ngOnInit(): void {

    this.dataService.getInspections()
      .subscribe( (inspections: any) => {
        this.insps = inspections;
      })

  }

}
