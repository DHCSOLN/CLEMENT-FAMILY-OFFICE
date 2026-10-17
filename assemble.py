import json,re,pathlib
root=pathlib.Path(__file__).resolve().parents[1]
h=(root/'src/base.html').read_text()
# Preserve the original owner interface and its source records; scope every data operation.
h=h.replace("fetch(","officeFetch(")
h=h.replace("state=d.state||structuredClone(SEED);upgradeRequirements();","state=d.state||(activeHousehold==='clement'?structuredClone(SEED):blankOffice());upgradeRequirements();")
h=h.replace('upgradeRequirements();etag=', 'upgradeRequirements();upgradeOfficeReadiness();const teamAdded=preparePeachtreeTeam();etag=')
h=h.replace("etag=d.etag;render()};function toast", "etag=d.etag;if(teamAdded)await save('Recorded Peachtree Planning as first proposed team, subject to agreement');else render()};function toast")
h=h.replace('function upgradeRequirements(){','function upgradeRequirements(){ensureOffice();if(activeHousehold!==\'clement\')return;')
h=h.replace("Math.round(done/state.tasks.length*100)","Math.round(done/Math.max(1,state.tasks.length)*100)")
h=re.sub(r"load\(\)\.catch\(e=>\{\$\('#app'\)\.textContent='Unable to load the private workspace\. '\+e\.message\}\);",'',h)
css='''<style>fieldset{border:1px solid var(--line);border-radius:7px;margin:14px 0;padding:10px}.check{display:inline-block;min-width:170px;margin:6px}.check input{width:auto;margin:0 8px 0 0}.agreementText{white-space:pre-wrap;font:14px/1.7 Georgia;overflow-wrap:anywhere}.top label{min-width:220px}.top select{margin-bottom:0}.actions{flex-wrap:wrap}details{margin:12px 0}summary{cursor:pointer;line-height:1.7}button:focus-visible,a:focus-visible{outline:3px solid #b29455;outline-offset:3px}</style>'''
templates='const AGREEMENT_TEMPLATES='+json.dumps(json.loads((root/'src/agreement-templates.json').read_text()),ensure_ascii=True)+';\n'
shared=templates+(root/'src/office.js').read_text()
wrap='''
const originalRender=render;
render=function(){ensureOffice();let output=extraOutput();if(page==='Shared document access')output=documentsPage();if(activeHousehold!=='clement'&&page==='Overview')output=neutralOverview();if(output===null){originalRender();}else{$('#app').innerHTML=output;const ps=activeHousehold==='clement'?pages:['Overview','Shared document access',...EXTRA_PAGES];$('#nav').innerHTML=ps.map(p=>'<button class="'+(p===page?'active':'')+'" onclick="page=\\''+p+'\\';render()">'+esc(p)+'</button>').join('')}scopeLinks()};
pages.push('Shared document access',...EXTRA_PAGES);
function neutralOverview(){return head(esc(currentHousehold().name),'Separate records, accounts, agreements and professional responsibilities.')+'<div class="notice">'+(currentHousehold().kind==='Charitable foundation'?'Charitable funds and donor restrictions are separate from private family entitlements.':'Only records assigned to this workspace are shown.')+'</div><div class="grid">'+[[state.ledgerAccounts.length,'Ledger accounts'],[state.journals.length,'Posted journals'],[state.documents.length,'Documents'],[state.agreements.length,'Agreements']].map(x=>'<div class="card"><div class="metric">'+x[0]+'</div>'+x[1]+'</div>').join('')+'</div><div class="card"><h2>Start with the operating records</h2><p class="muted">Add separately titled accounts, governing documents, professional engagements and service agreements. No Clement family records or assets are copied into this workspace.</p></div>'}
startOffice().catch(e=>{$('#app').textContent='Unable to load the private workspace. '+e.message});
'''
h=h.replace('</style>', '</style>'+css,1)
h=h.replace('</script></html>',shared+wrap+'</script></html>')
# A separate portal prevents owner-only inline seed / trust migration data reaching other users.
style=re.search(r'<style>(.*?)</style>',h,re.S)[0]+css
body='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Family Office • Assigned Workspace</title>'''+style+'''<aside><div class="crest">C</div><div class="brand">Family Office</div><div class="sub">PROFESSIONAL & FAMILY PORTAL</div><nav id="nav"></nav><footer>Individual access<br>Assigned workspaces only</footer></aside><main><div class="top"></div><div id="app">Checking your assignment…</div></main><dialog id="modal"></dialog><div id="toast" role="status"></div><script>'''
helper=re.search(r"const \$=s=>document.querySelector\(s\),esc=.*?;\n",h,re.S)[0]
forms=re.search(r'function head\(.*?\n',h)[0].replace('Clement family office','Family office')
shared_member=re.sub(r'function accessPage\(\)\{[\s\S]*?(?=function agreementsPage\()',"function accessPage(){return head('Your assigned access','Permissions apply only to your own assigned workspaces.')+'<div class=\"card\">'+currentHousehold().grants.map(g=>'<h3>'+esc(g.role)+'</h3><p>'+esc(g.firm||'Individual appointment')+'</p>'+['read','edit','approve'].map(k=>'<p>'+k+': '+(g[k].map(m=>MODULE_LABELS[m]).join(', ')||'None')+'</p>').join('')).join('')+'</div>'}\n",shared)
shared_member=re.sub(r'function upgradeOfficeReadiness[\s\S]*$', '', shared_member)
member='''let state,etag,page='Overview',websiteArchive=null;'''+helper+forms+'''
function toast(t){$('#toast').textContent=t;$('#toast').style.display='block';setTimeout(()=>$('#toast').style.display='none',4000)}
async function fileHash(file){return [...new Uint8Array(await crypto.subtle.digest('SHA-256',await file.arrayBuffer()))].map(x=>x.toString(16).padStart(2,'0')).join('')}
async function load(){const r=await officeFetch('/api/state'),d=await r.json();if(!r.ok)throw Error(d.error);state={...blankOffice(),...d.state};etag=d.etag;render()}
const MODULE_FIELDS={records:['entities','assets','archiveRecords','books','sources'],finance:['transactions','scorecards','growth','ledgerAccounts','journals','reserveImports','transactionRequests'],tax:['taxReturns'],legal:['constitution','constitutionVersion','trustPlans','familyPolicy','legacyReviews'],beneficiaries:['beneficiaries'],documents:['documents'],agreements:['agreements'],coverage:['professionalCoverage'],programs:['philanthropyPrograms'],planning:['tasks','expansionPlans','familyProspects']};
async function save(action){const patch={};for(const [m,keys] of Object.entries(MODULE_FIELDS))if(permitted('edit',m))for(const k of keys)patch[k]=k==='documents'?(state.documents||[]).filter(d=>d.accessModule&&permitted('edit',d.accessModule)&&!d.sourceId):state[k];const r=await officeFetch('/api/state',{method:'PUT',headers:{'Content-Type':'application/json','If-Match':etag||'new'},body:JSON.stringify(patch)}),d=await r.json();if(!r.ok){await load();throw Error(d.error||'Save failed')}etag=d.etag;toast('Saved to assigned workspace');render()}
'''+shared_member+'''
function render(){ensureOffice();const available=['Overview','Access & administration'];if(permitted('read','documents'))available.push('Documents');if(permitted('read','agreements'))available.push('Agreements');if(permitted('read','coverage'))available.push('Professional team');if(permitted('read','finance'))available.push('Ledger & accounts','Transaction requests','Reserve connection');available.push('Approvals');for(const m of ['records','tax','legal','beneficiaries','programs','planning'])if(permitted('read',m))available.push(MODULE_LABELS[m]);$('#nav').innerHTML=available.map(p=>'<button class="'+(p===page?'active':'')+'" onclick="page=\\''+p+'\\';render()">'+esc(p)+'</button>').join('');let out=extraOutput();if(page==='Documents')out=documentsPage();const m=Object.keys(MODULE_LABELS).find(m=>MODULE_LABELS[m]===page);if(m)out=genericRecordsPage(m);if(page==='Overview')out=head(esc(currentHousehold().name),'Your individual assignment controls available records, documents and balances.')+'<div class="card"><h2>Work within your assigned scope</h2><p class="muted">Use the navigation to view permitted records, prepare work and request independent review. Bank signing, investment discretion and fiduciary authority require separate documented appointments.</p></div>';$('#app').innerHTML=out||'<p>No records available in this work area.</p>';scopeLinks()}
startOffice().catch(e=>{$('#app').textContent='Unable to load assigned workspace. '+e.message});
'''
member=body+member+'</script></html>'
(root/'worker/index.js').write_text('const HTML='+json.dumps(h)+';\nconst MEMBER_HTML='+json.dumps(member)+';\n'+(root/'src/backend.js').read_text())
print('Assembled owner and assigned-user portals')
