import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { TableComponent } from './components/table/table.component';
import { ResumeComponent } from './components/resume/resume.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { MatTableModule } from "@angular/material/table";

@NgModule({
  declarations: [
    AppComponent,
    TableComponent,
    ResumeComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatTableModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
